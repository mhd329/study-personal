import cafe.ade.LemonAde;
import cafe.ade.OrangeAde;
import cafe.coffee.Americano;
import cafe.coffee.CafeLatte;


public class App {

	public static void main(String[] args) {
		LemonAde la = new LemonAde();
		la.printInfo();
		OrangeAde oa = new OrangeAde();
		oa.printInfo();
		Americano a = new Americano();
		a.printInfo();
		CafeLatte c = new CafeLatte();
		c.printInfo();

	}

}
