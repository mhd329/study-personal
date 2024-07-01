package classtest.daySpace;

public class DaySpace {

	public static void main(String[] args) {
		String dayStr = "일,월,화,수,목,금,토";
		String tap = "";
		for (String s: dayStr.split(",")) {
			System.out.println(tap+s+"요일");
			tap += "\t";
		}

	}

}
