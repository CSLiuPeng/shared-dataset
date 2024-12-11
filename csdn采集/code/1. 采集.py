import time

import copyheaders
import pandas
import requests

headers = copyheaders.headers_raw_to_dict(b"""
accept:application/json, text/plain, */*
cookie:uuid_tt_dd=10_20282717530-1732796805193-142235; fid=20_95498485114-1732796805903-521280; loginbox_strategy=%7B%22taskId%22%3A349%2C%22abCheckTime%22%3A1732796806733%2C%22version%22%3A%22exp11%22%2C%22blog-threeH-dialog-exp11tipShowTimes%22%3A1%2C%22blog-threeH-dialog-exp11%22%3A1732796806734%7D; UserName=qq_41677333; UserInfo=b1f163e2519c427b8f0b1860327ee2c7; UserToken=b1f163e2519c427b8f0b1860327ee2c7; UserNick=961948438; AU=FF1; UN=qq_41677333; BT=1732796825417; p_uid=U010000; tfstk=f5Nsdsqt4hx_dZ6NFEQEAxP8vlhb1o1z6EgYrrdwkfhTkjaYomoZ3myIcrE-3xUVSqEQklZZ3GsiGZZ30NVabSwHGz40_NcVSf4iijIP4_lbSPcD35Tt85tK94zp6hdYVn_fwjIP46-WJskxMlrcI39QJD0jkm3YDDCKx4OxMcHvvp3-vjnYDcnp94gtDI3tMDQIoDnxMjh-oHgVCqU18Zl3u-Rn8PnBNyVIWim5ZDdvTWg_R0UTeIdYOVM_iqFLCJHaHzDu_rfXtfz7pX3zS1OIwP37bDrRwBGL8yEqEJjDavqQGxFtIEI-2xi_p5HBkIUnGcMuhls6IceaAY0KpE1o8uoLS5eCoHUT4cGtJv5RPyHYL5Du_Mdsw84Z_-EcUpc_kRhC4GArVyAvheMkG2iPRw9Dnbq2szBPDfWnB20Oaw_BAKDt-2wlRw9DsA3nWS7CRLAV.; csdn_newcert_qq_41677333=1; c_dl_fref=https://so.csdn.net/so/search; c_dl_prid=1733316488565_978495; c_dl_rid=1733316851064_766125; c_dl_fpage=/download/weixin_38538950/14872062; c_dl_um=distribute.pc_search_result.none-task-blog-2%7Eall%7Esobaiduend%7Edefault-1-122065189-null-null.142%5Ev100%5Epc_search_result_base6; historyList-new=%5B%5D; redpack_close_time=1; firstDie=1; https_waf_cookie=797b90d1-dc91-402d7e3f7def90d58bfeff6c12bfc4e54b36; dc_session_id=10_1733886798623.711242; csrfToken=KHvMOX1yBeLK4BJSlRs5uHhO; c_pref=default; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/nav/lang; c_dsid=11_1733886797297.508304; c_segment=11; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1733726833,1733810460,1733813170,1733886798; HMACCOUNT=21C63CB5C70336B9; is_advert=1; creativeSetApiNew=%7B%22toolbarImg%22%3Anull%2C%22publishSuccessImg%22%3Anull%2C%22articleNum%22%3A0%2C%22type%22%3A0%2C%22oldUser%22%3Afalse%2C%22useSeven%22%3Afalse%2C%22oldFullVersion%22%3Afalse%2C%22userName%22%3A%22qq_41677333%22%7D; dc_sid=b1cbb3a4ac05e7a4f4d886caf5c25092; __gads=ID=1bcad5660428e65a:T=1732892587:RT=1733886801:S=ALNI_MasFa2ctoANDVECk2-5huR5mOq-bg; __gpi=UID=00000f7a59025d3c:T=1732892587:RT=1733886801:S=ALNI_MY328XgMIM5k405c0qfO7S7LDrYPw; __eoi=ID=4d52d278ea62a611:T=1732892587:RT=1733886801:S=AA-AfjYBgeRl5KsgsAcNEzmW8UCi; c_ref=https%3A//blog.csdn.net/nav/lang; c_page_id=default; log_Id_pv=2; cms_blog_nav_flag=true; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1733886836; log_Id_view=185; _clck=1rhcit4%7C2%7Cfrm%7C0%7C1793; _clsk=1e9jkrm%7C1733886838034%7C1%7C0%7Cu.clarity.ms%2Fcollect; dc_tos=sob7na; FCNEC=%5B%5B%22AKsRol9Mky9MUUg3aFEF9L4gcTFCu2fBA7w8RlDrKJLjSBSPZY2JoXMgK3QF-raV8L5Bn6QWhaou605oNeCaY_-tZzaSKzJWr8pvLr3LrmeCIoyXAhJdnqEGnknUbRKrhO6VRUPRKvYF-_qjeDwVFw6lMMrxF6Cmsw%3D%3D%22%5D%5D; waf_captcha_marker=75d6cd070868da4bd0fa5fa3cb92e60c13da2309e0da672cf9c5c2ba26c9f298; cms_blog_nav={%22cate1%22:%22web%22%2C%22cate2%22:{%22type%22:%22javascript%22%2C%22title%22:%22javascript%22}}; log_Id_click=2
referer:https://blog.csdn.net/nav/web
user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0
""")


def send_get(url,headers,params):
    while 1:
        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=(10,10)
            )
            time.sleep(.5)
            return response
        except Exception as e:
            print(f'some error:{e}')
            time.sleep(1)

def download_data():

    data_rs = []
    for cate1,cate2 in [
        ('前端', 'javascript'),
        ('前端', 'ajax'),
        ('前端', 'css'),
        ('前端', 'css3'),
        ('前端', 'regex'),
        ('前端', 'html'),
        ('前端', 'html5'),
        ('前端', 'react.js'),
        ('前端', 'postman'),
        ('前端', 'web'),
        ('前端', 'npm'),
        ('前端', 'chrome'),
        ('前端', 'node.js'),
        ('前端', 'vue.js'),
        ('前端', 'web-frame'),
        ('前端', 'typescript'),
        ('前端', 'elementui'),
        ('前端', 'ecmascript'),
        ('前端', 'webpack'),
        ('前端', 'echarts'),
        ('前端', 'jquery'),
        ('前端', 'json'),

        ('编程语言', 'ruby'),
        ('编程语言', 'javascript'),
        ('编程语言', 'java'),
        ('编程语言', 'swift'),
        ('编程语言', 'bash'),
        ('编程语言', 'c'),
        ('编程语言', 'scala'),
        ('编程语言', 'r'),
        ('编程语言', 'rust'),
        ('编程语言', 'qt'),
        ('编程语言', 'dev-lang'),
        ('编程语言', 'python'),
        ('编程语言', 'golang'),
        ('编程语言', 'php'),
        ('编程语言', 'objective-c'),
        ('编程语言', 'csharp'),
        ('编程语言', 'cpp'),
        ('编程语言', 'matlab'),
        ('编程语言', 'kotlin'),

    ]:
        for page in range(1,300):
            url = "https://cms-api.csdn.net/v1/web_home/select_content"
            params = {
                "componentIds": "www-blog-recommend",
                "cate1": cate1,
                "cate2": cate2
            }
            response = send_get(url,headers,params)

            datas = response.json().get("data",{}).get("www-blog-recommend",{}).get("info",[])


            for idata in datas:

                extend_data = idata.get("extend")

                saveitem = {}
                saveitem["一级分类"] = cate1
                saveitem["二级分类"] = cate2
                saveitem["标题"]  = extend_data.get("title")
                saveitem["描述"]  = extend_data.get("desc")
                saveitem["发布者码龄"]  = extend_data.get("user_days")
                saveitem["发布者"]  = extend_data.get("nickname")
                saveitem["发布时间"]  = extend_data.get("created_at")
                saveitem["阅读数"]  = extend_data.get("views")
                saveitem["评论数"]  = extend_data.get("comments")

                print(page,saveitem)

                data_rs.append(saveitem)

    df = pandas.DataFrame(data_rs)
    df.to_excel("原始数据表.xlsx",index=False)



if  __name__ == '__main__':


    download_data()