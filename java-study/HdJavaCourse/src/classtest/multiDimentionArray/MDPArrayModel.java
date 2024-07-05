package classtest.multiDimentionArray;

public class MDPArrayModel {
	// 단일 객체만 사용
	private static MDPArrayModel pam = new MDPArrayModel();
	
	// 가져오는 메서드
	public static MDPArrayModel getPersonArrayInstance() {
		return pam;
	}

	// 2차원 Person 배열
	private Person[][] MDPArray;
	
	// 이 아래부턴 클래스 필드 정의
	private MDPArrayModel() {
//		pam.MDPArray = new Person[2][];
//		-> 여기는 생성자고, instance가 생성되지 않음(생성되는 중)
//		-> 여기서 pam을 호출하게 되면 nullPointerException이 발생함
//		-> 따라서 아래와 같이 this를 사용해야 함
		this.MDPArray = new Person[2][];
	}
	
	public Person[][] setPersonArrayValues(int idx0, int idx1, String name, int age) {
		// 아래는 가변 2차원 배열에 대한 코드
		if (pam.MDPArray[idx0] == null) {
			pam.MDPArray[idx0] = new Person[idx1 + 1];
		}
		int oldArrayLength = pam.MDPArray[idx0].length;
		if (idx1 >= oldArrayLength) {
			Person[] newPersonArray = new Person[idx1 + 1];
			System.arraycopy(pam.MDPArray[idx0], 0, newPersonArray, 0, oldArrayLength);
			pam.MDPArray[idx0] = newPersonArray;
		}
		pam.MDPArray[idx0][idx1] = new Person(name, age);
		return pam.MDPArray;
	}
	
//	public Person[] setPersonArray(Person[] personArray) {
//		pac.personArray = personArray;
//		return pac.personArray;
//	}
	
	public Person getPersonArrayEachValue(int idx0, int idx1) {
		return pam.MDPArray[idx0][idx1];
	}
	
	public Person[][] getPersonArray() {
		return pam.MDPArray;
	}
	
	public Person[] getPersonArray(int i) {
		return pam.MDPArray[i];
	}
	
}
