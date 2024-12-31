from witshape import version
from cmdbox.app import common, feature
from cmdbox.app.features.web import cmdbox_web_exec_cmd
from cmdbox.app.web import Web
from fastapi import FastAPI, Request, Response, HTTPException


class PgvectorSearch(cmdbox_web_exec_cmd.ExecCmd):
    def route(self, web:Web, app:FastAPI) -> None:
        """
        webモードのルーティングを設定します

        Args:
            web (Web): Webオブジェクト
            app (FastAPI): FastAPIオブジェクト
        """
        @app.post('/pgvector_search/retrieval')
        @app.get('/pgvector_search/retrieval')
        async def pgvector_search(req:Request, res:Response):
            signin = web.check_apikey(req, res)
            if signin is not None:
                raise HTTPException(status_code=401, detail=self.DEFAULT_401_MESSAGE)
            try:
                json_data = await req.json()
                if json_data is None:
                    raise Exception("No JSON data")
                knowledge_id = json_data.get("knowledge_id", None)
                query = json_data.get("query", None)
                retrieval_setting = json_data.get("retrieval_setting", None)
                if retrieval_setting is None:
                    retrieval_setting = dict()
                top_k = retrieval_setting.get("top_k", 5)
                score_threshold = retrieval_setting.get("score_threshold", 0)

                opt = self.load_cmd(web, knowledge_id)
                opt['query'] = query
                opt['kcount'] = top_k
                opt['score_th'] = score_threshold
                opt['capture_stdout'] = nothread = True
                opt['stdout_log'] = False
                res = self.exec_cmd(req, res, web, 'pgvector', opt, nothread=True, appcls=self.appcls)
                recodes = []
                if res is not None and type(res) is list:
                    for message in res:
                        if message is None or type(message) is not dict: continue
                        if 'success' not in message: continue
                        if type(message['success']) is not dict: continue
                        if 'docs' not in message['success']: continue
                        if type(message['success']['docs']) is not list: continue
                        for doc in message['success']['docs']:
                            d = dict(metadata=dict(path="",description=""),
                                     score=0.5,
                                     title="",
                                     content=doc['content'])
                            recodes.append(d)
                ret = dict(records=recodes)
                return ret
            except Exception as e:
                web.logger.warning(f"Error: {e}", exc_info=True)
                raise HTTPException(status_code=400, detail=self.DEFAULT_400_MESSAGE)
