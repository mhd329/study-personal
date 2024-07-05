package classtest;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateUtil {
	/**
	 * 현재 일자 및 시간을 리턴한다.
	 * 
	 * @param
	 * @return String
	 */
	public static String getLocalDateTimeDash() {
	LocalDateTime now = LocalDateTime.now();
	DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("YYYY-MM-dd E HH:mm:ss");
	return now.format(dateTimeFormatter);
	}
	
}