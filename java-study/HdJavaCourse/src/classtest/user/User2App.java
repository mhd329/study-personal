package classtest.user;

public class User2App {

	public static void main(String[] args) {
		String name = "Lee";
		int age = 20;
		float height = 180.5f;
		char sex = 'M';
		boolean marriageYn = true;
		
		System.out.println("프린트인포");
		User2 user2 = new User2(name, age, height, sex, marriageYn);
		user2.printInfo();

	}

}
