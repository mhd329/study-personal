package classtest.multiDimentionArray;

public class MDArrayApp {

	public static void main(String[] args) {
		MDArray mda = new MDArray();
		int arrSize = mda.getMDArrSize();
		System.out.printf("Arr size is %d\n", arrSize);
		mda.getMDArrEachValues();
		
	}

}
