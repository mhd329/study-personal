package classtest.car;

public class Company {
	private String name;
	private String biz;
	
	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getBiz() {
		return this.biz;
	}

	public void setBiz(String biz) {
		this.biz = biz;
	}

	public Company(String name, String biz) {
		this.setName(name);
		this.setBiz(biz);
	}
	
	public void printInfo() {
		System.out.printf("회사명=%s | 사업분야=%s\n", this.getName(), this.getBiz());
	}
}
