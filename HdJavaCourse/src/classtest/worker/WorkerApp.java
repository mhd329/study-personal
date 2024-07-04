package classtest.worker;

public class WorkerApp {

	public static void main(String[] args) {
		Worker w1 = new Worker("Rose", 3, Job.PROGRAMMER);
		Worker w2 = new Worker("James", 10, Job.WEB_DESIGNER);
		Worker w3 = new Worker("Paige", 15, Job.UI_DESIGNER);

		w1.printInfo();
		w2.printInfo();
		w3.printInfo();
	}

}
