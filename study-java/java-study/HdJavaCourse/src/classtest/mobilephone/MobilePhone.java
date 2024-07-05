package classtest.mobilephone;

public class MobilePhone {
	// int type parameters
	private int memory;
	private int storage;
	private int battery;
	
	// String type parameters
	private String company;
	private String name;
	private String os;
	private String color;
	
	// boolean type parameters
	private boolean pen;
	
	
	// getters
	public int getMemory() {
		return this.memory;
	}
	
	public int getStorage() {
		return this.storage;
	}
	
	public int getBattery() {
		return this.battery;
	}
	
	public String getCompany() {
		return this.company;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getOs() {
		return this.os;
	}
	
	public String getColor() {
		return this.color;
	}
	
	public boolean isPenSupport() {
		return this.pen;
	}

	// setters
	public void setMemory(int memory) {
		if (memory < 1) {
			System.out.println("메모리는 0보다 커야합니다.");
			return;
		}
		this.memory = memory;
	}
	
	public void setStorage(int storage) {
		if (storage < 1) {
			System.out.println("저장 용량은 0보다 커야합니다.");
			return;
		}
		this.storage = storage;
	}
	
	public void setBattery(int battery) {
		if (battery < 1) {
			System.out.println("배터리 용량은 0보다 커야합니다.");
			return;
		}
		this.battery = battery;
	}
	
	public void setCompany(String company) {
		this.company = company;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setOs(String os) {
		this.os = os;
	}
	
	public void setColor(String color) {
		this.color = color;
	}
	
	public void setPen(boolean pen) {
		this.pen = pen;
	}
	
	public void printInfo() {
		System.out.println(this.company);
		System.out.println(this.name);
		System.out.println(this.os);
		System.out.println(this.color);
		if (this.isPenSupport()) {
			System.out.println("지원");
		} else {
			System.out.println("미지원");
		}
		System.out.println(this.memory);
		System.out.println(this.storage);
		System.out.println(this.battery);
	}
}
