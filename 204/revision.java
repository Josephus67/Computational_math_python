
public class revision {

    public static void main(String[] args) {
        int[] arr = {254, 2, 12, 3, 45, 87, 12, 89, 22};
        int max = arr[0]; 

        for (int i = 0; i < arr.length; i++) { 
            if (arr[i] > max) {
                max = arr[i]; 
            }
        }

        System.out.println("The maximum number is: " + max);
        
    }
}