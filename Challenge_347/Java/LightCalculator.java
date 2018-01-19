import java.util.BitSet;
import java.lang.Math;
public class LightCalculator{
    private static int[][] inputOne = {
        {2,4},
        {3,6},
        {1,3},
        {6,8}
    };

    private static int[][] inputTwo = {
        {6,8},
        {5,8},
        {8,9},
        {5,7},
        {4,7}
    };

    private static int[][] inputThree = {
        {15,18},
        {13,16},
        {9,12},
        {3,4},
        {17,20},
        {9,11},
        {17,18},
        {4,5},
        {5,6},
        {4,5},
        {5,6},
        {13,16},
        {2,3},
        {15,17},
        {13,14},
    };

    public static void main(String... args){
        System.out.println(calculateTimeOn(inputOne));
        System.out.println(calculateTimeOn(inputTwo));
        System.out.println(calculateTimeOn(inputThree));
    }

    public static int calculateTimeOn(int[][] timeFrames){
        BitSet finalTimeFrame = new BitSet();
        for (int[] frame : timeFrames){
            // Gets the max amount of time slots needed for this specific frame
            BitSet tempFrame = new BitSet(Math.max(frame[0],frame[1]));
            // Set hours the light is on for the this current time frame
            for (int i = Math.min(frame[0],frame[1]) + 1; i <= Math.max(frame[0],frame[1]); i++){
                tempFrame.set(i);
            }
            // Add the times to the overall time frame
            finalTimeFrame.or(tempFrame);
        }
        return finalTimeFrame.cardinality();
    }
}
