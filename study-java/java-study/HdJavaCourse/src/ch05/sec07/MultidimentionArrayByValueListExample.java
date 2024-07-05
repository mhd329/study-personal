package ch05.sec07;

public class MultidimentionArrayByValueListExample {

	public static void main(String[] args) {
		int[][] scores = {
			{80, 90, 96},
			{76, 88}
		};

		System.out.printf("[] : %d\n", scores.length);
		System.out.printf("[0][] : %d\n", scores[0].length);
		System.out.printf("[1][] : %d\n", scores[1].length);
		
		int c1sum = 0;
		int c1len = scores[0].length;
		int c2sum = 0;
		int c2len = scores[1].length;
		
		for (int i = 0; i < c1len; i ++) {
			c1sum += scores[0][i];
		}
		for (int i = 0; i < c2len; i ++) {
			c2sum += scores[1][i];
		}
		
		double c1avg = (double) c1sum / c1len;
		double c2avg = (double) c2sum / c2len;
		
		System.out.println(c1avg);
		System.out.println(c2avg);
		
		int tt = 0;
		int tts = 0;
		
		for (int i = 0; i < scores.length; i ++) {
			tts += scores[i].length;
			for (int j: scores[i]) {
				tt += j;
			}
		}
		
		System.out.println((double) tt / tts);
		
	}

}
