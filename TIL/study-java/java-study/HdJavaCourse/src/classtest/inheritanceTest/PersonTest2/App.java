package classtest.inheritanceTest.PersonTest2;

public class App {

    public static void main(String[] args) {

    	Person[] personArray = new Person[3];
    	personArray[0] = new Person("Paige", 20);
    	personArray[1] = new Student("James", 30, "2023-001");
    	personArray[2] = new Teacher("Victoria", 40, "Music");

    	System.out.println("===== printInfo() =====");
    	for (int i = 0; i < personArray.length; i ++) {
    		personArray[i].printInfo();
    	}

    }
    
}