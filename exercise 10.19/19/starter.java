import java.util.Scanner;
import java.util.Random;

class starter {
	public static int mult(int a, int b){
		int x = a;
		int y = b;
		System.out.println(x*y);
		int g = x*y;
		
		if (g%3==0){
			System.out.println("The answer is divisible by 3");
			
		}
		else {
			System.out.println("The answer is not divisible by 3");
			
		}
		return g; 
		
	}
	public static void main(String args[]) {
		// Your code goes below here
	Scanner sc = new Scanner(System.in);
	System.out.print("Enter an integer ");
	int first = sc.nextInt();
	sc.nextLine();
	System.out.print("Enter another integer ");
	int sec = sc.nextInt();
	mult(first,sec);
	


		
	}
}
