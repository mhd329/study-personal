package classtest.person;

public class PersonArrayApp {

	public static void main(String[] args) {
		PersonArray pac = PersonArray.getPersonArrayInstance();
		pac.setPersonArrayValues(0, "Hong", 25);
		pac.setPersonArrayValues(1, "Lee", 40);
		pac.setPersonArrayValues(2, "Park", 35);

		for (int i = 0; i < 3; i ++) {	
			pac.getPersonArrayValues(i).printInfo();
		}
		
	}

}
