package classtest.inheritanceTest.PersonTest2;

public class Biz {

    // ==================================================
    // - 첫번째 if 문만 실행된다.
    // ==================================================
    public void top(Person person) {

        if (person instanceof Person) {
            System.out.println("Person");
        } else if (person instanceof Student) {
            System.out.println("Student");
        } else if (person instanceof Teacher) {
            System.out.println("Teacher");
        }

    }

    // ==================================================
    // - Teacher 객체는 1번 if 문에서 처리
    // - Student 객체는 2번 if 문에서 처리
    // - Person 객체는 3번 if 문에서 처리
    // ==================================================
    public void down(Person person) {

        if (person instanceof Teacher) {
            System.out.println("Teacher");
        } else if (person instanceof Student) {
            System.out.println("Student");
        } else if (person instanceof Person) {
            System.out.println("Person");
        }

    }

}