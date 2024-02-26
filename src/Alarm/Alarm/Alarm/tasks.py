from apscheduler.schedulers.background import BackgroundScheduler
from parser import post_latest_data
from datetime import datetime
scheduler = BackgroundScheduler()


def update_data():
    # 데이터 업데이트 작업 수행
    #post_latest_data()
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'),"  크롤링 완료")
    
    #pass


# 스케줄링 작업 등록
scheduler.add_job(update_data, 'interval', minutes=1)


# 스케줄링 작업 실행
#scheduler.start()