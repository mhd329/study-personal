package classtest.multiDimentionArray;

public class MDArray {
	private int[][] intArr = new int[2][];
	
	public MDArray() {
		this.intArr[0] = new int[2];
		this.intArr[1] = new int[3];
		
		this.intArr[0][0] = 0;
		this.intArr[0][1] = 1;
		
		this.intArr[1][0] = 10;
		this.intArr[1][1] = 11;
		this.intArr[1][2] = 12;
	}
	
	public int getMDArrSize() {
		return intArr[0].length;
	}
	
	public void getMDArrEachValues() {
		for (int i = 0; i < intArr.length; i ++) {
			for (int j: intArr[i]) {				
				System.out.println(j);
			}
		}
	}
}
