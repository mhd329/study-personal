package classtest.salaryManagerApp;

public class SalaryManager {
	private Employee[] emps;
	public SalaryManager(Employee[] emps) {
		this.emps = emps;
	}
	public void printInfo() {
		for (Employee e: this.emps) {
			String empNum = e.getEmpNum();
			String name = e.getEmpName();
			int income = e.getEmpIncome();
			int score = e.getEmpScore();
			char grade = e.getEmpGrade();
			int nextYearIncome = e.getEmpNextYearIncome();
			System.out.printf("사번=%s\t|\t이름=%-10s\t|\t연봉=%d\t|\t사원평가=%s\t|\t등급=%c\t|\t내년연봉=%d\n", empNum, name, income, score, grade, nextYearIncome);
		}
	}
}
