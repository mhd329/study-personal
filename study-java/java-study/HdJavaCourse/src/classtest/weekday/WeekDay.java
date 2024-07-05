package classtest.weekday;

public class WeekDay {
	public static void main(String[] args) {		
		String[] weekDayArr;
		weekDayArr = new String[7];
		weekDayArr[0] = "월";
		weekDayArr[1] = "화";
		weekDayArr[2] = "수";
		weekDayArr[3] = "목";
		weekDayArr[4] = "금";
		weekDayArr[5] = "토";
		weekDayArr[6] = "일";
		
		for (int i = 0; i < weekDayArr.length; i ++) {
			System.out.printf("weekDay[%d] : %s요일\n", i, weekDayArr[i]);
		}
	}

}
