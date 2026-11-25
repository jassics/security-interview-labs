import java.io.IOException;

/**
 * Template for stdin/stdout judges (HackerRank, HackerEarth and similar).
 *
 * Example input:  3 newline 1 2 3     Example output: 6
 * Read the problem's input format carefully and change main() to match it.
 *
 * Compile and run:
 *   javac StdinTemplate.java && echo "3 1 2 3" | java StdinTemplate
 */
public class StdinTemplate {
    // Keep the real logic in a method like this one so it is easy to test.
    static long solve(long[] numbers) {
        long total = 0;
        for (long value : numbers) {
            total += value;
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        String all = new String(System.in.readAllBytes()).trim();
        String[] tokens = all.split("\\s+");
        int n = Integer.parseInt(tokens[0]);
        long[] numbers = new long[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = Long.parseLong(tokens[1 + i]);
        }
        System.out.println(solve(numbers));
    }
}
