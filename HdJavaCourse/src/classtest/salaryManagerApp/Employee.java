package classtest.salaryManagerApp;

public class Employee {
	private String empNum;
	private String empName;
	private int empIncome;
	private int empScore;
	private char empGrade; // 근무 평가
	private int empNextYearIncome; // 내년 연봉
	
	public String getEmpNum() {
		return empNum;
	}
	public void setEmpNum(String empNum) {
		this.empNum = empNum;
	}
	public String getEmpName() {
		return empName;
	}
	public void setEmpName(String empName) {
		this.empName = empName;
	}
	public int getEmpIncome() {
		return empIncome;
	}
	public void setEmpIncome(int empIncome) {
		this.empIncome = empIncome;
	}
	public int getEmpScore() {
		return empScore;
	}
	public void setEmpScore(int empScore) {
		this.empScore = empScore;
	}
	public char getEmpGrade() {
		return empGrade;
	}
	public int getEmpNextYearIncome() {
		return empNextYearIncome;
	}
	
	private void setEmpGrade() {
		switch ((int) this.empScore / 5) {
			case 19 -> { // 95 or over
				this.empGrade = 'S';
			}
			case 18 -> { // 90 or over
				this.empGrade = 'A';
			}
			case 17, 16 -> { // 80 or over
				this.empGrade = 'B';
			}
			case 15, 14 -> { // 70 or over
				this.empGrade = 'C';
			}
			default -> {
				this.empGrade = 'D';
			}
		}
	}
	
	private int convertIncome(double c) {
		double income = (double) this.empIncome;
		double add = Math.round(income * c);
		int result = (int) (income + add);
		return result;
	}
	
	private void setEmpNextYearIncome() {
		switch (this.empGrade) {
			case 'S' -> {
				this.empNextYearIncome = this.convertIncome(0.15);
			}
			case 'A' -> {
				this.empNextYearIncome = this.convertIncome(0.10);
			}
			case 'B' -> {
				this.empNextYearIncome = this.convertIncome(0.05);
			}
			case 'C' -> {
				this.empNextYearIncome = this.convertIncome(0.03);
			}
			default -> {
				this.empNextYearIncome = this.convertIncome(0);
			}
		}
//		this.empIncome;
//		this.empNextYearIncome;
	}
	
	public Employee(String empNum, String empName, int empIncome, int empScore) {
		this.setEmpNum(empNum);
		this.setEmpName(empName);
		this.setEmpIncome(empIncome);
		this.setEmpScore(empScore);
		this.setEmpGrade();
		this.setEmpNextYearIncome();
	}
	
}
