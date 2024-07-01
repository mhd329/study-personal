package classtest.person;

public class PersonArray {
	// 단일 객체만 사용
	private static PersonArray pac = new PersonArray();
	
	// 가져오는 메서드
	public static PersonArray getPersonArrayInstance() {
		return pac;
	}
	
	// 이 아래부턴 클래스 필드 정의
	Person[] personArray;
	
	private PersonArray() {
		this.personArray = new Person[3];
	}
	
	public Person[] setPersonArrayValues(int idx, String name, int age) {
		pac.personArray[idx] = new Person(name, age);
		return pac.personArray;
	}
	
//	public Person[] setPersonArray(Person[] personArray) {
//		pac.personArray = personArray;
//		return pac.personArray;
//	}
	
	public Person getPersonArrayValues(int idx) {
		return pac.personArray[idx];
	}
	
	public Person[] getPersonArray() {
		return pac.personArray;
	}
	
}
