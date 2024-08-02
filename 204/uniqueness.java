public class uniqueness {
    public static void main(String [] args){
        int[] arr={1,2,3,4,2};
        int check=arr[0];
        for (int i=0; i<arr.length; i++){
            if (check==arr[i]){
                //check=arr[i];
                System.out.println(check+" is not unique");
            }
            else{
                System.out.println("it is unique");
            }
        }
    }
}
