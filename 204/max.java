public class max {
    public static void main(String [] args){
        int[] arr={1,2,5,6,3,8,12,43,90,4,6,23,3434,80};
        int maxValue=arr[0];
        for (int i=0; i<arr.length; i++){
            if (arr[i]>maxValue){
                maxValue=arr[i];    
            }
        }
        System.out.println(maxValue);
    }
}
