package classtest.order;

import java.text.DecimalFormat;

public class DecimalUtil {

/**
 * 3자리마다 콤마를 찍는다.
 * 
 * @param input 숫자
 * @return
 */
public static String decimalComma(int input) {
	DecimalFormat df = new DecimalFormat("#,##0");
	String result = df.format(input);
	return result;
	}
}