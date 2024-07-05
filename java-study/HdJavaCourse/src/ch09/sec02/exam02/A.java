package ch09.sec02.exam02;

public class A {
	class B {
		int f1 = 1;
		static int f2 = 2;
		B() {
			System.out.println("B 생성자 실행");
		}
		void method1() {
			System.out.println("B 메솓1");
		}
		static void method2() {
			System.out.println("B 메솓2");
		}
	}
	void useB() {
		B b = new B();
		System.out.println(b.f1);
		b.method1();
		System.out.println(B.f2);
		B.method2();
	}
}
