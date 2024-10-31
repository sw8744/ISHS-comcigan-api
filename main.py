from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pycomcigan import *
from datetime import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

table = TimeTable('인천과학고등학교', 1)
start = datetime(*map(int, table.start_date.split('-')))
@app.get("/{grade}/{class_}")
def read_root(grade, class_):
    grade = int(grade)
    class_ = int(class_)
    timetable = TimeTable("인천과학고", week_num=0)
    weekList = [timetable.MONDAY, timetable.TUESDAY, timetable.WEDNESDAY, timetable.THURSDAY, timetable.FRIDAY]
    weekday = datetime.today().weekday()
    if weekday == 5 or weekday == 6:
        return {"error": "WeekendError"}
    else:
        return timetable.timetable[grade][class_][weekList[weekday]]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000)