package classtest.multiDimentionArray;

public class MDPArrayApp {
	public static void main(String[] args) {
		MDPArrayModel pam = MDPArrayModel.getPersonArrayInstance();
		pam.setPersonArrayValues(0, 0, "Hong", 25);
		pam.setPersonArrayValues(1, 0, "Lee", 40);
		pam.setPersonArrayValues(1, 1, "Park", 35);

		int x = pam.getPersonArray().length;
		
		for (int i = 0; i < x; i ++) {
			Person[] y = pam.getPersonArray(i);
			System.out.printf("이번 배열의 길이 : %d\n", y.length);
			for (Person j: y) {
				if (j == null) {
					System.out.println("값이 없습니다.");
					continue;
				}
				j.printInfo();
			}
		}
		
	}
}
