import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;

public class HelloWorld {
    public static void main(String[] args) {
        String logFilePath = "/logs/hello_world.log";
        String message = "Hello, World! Timestamp: " + LocalDateTime.now();

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(logFilePath, true))) {
            writer.write(message);
            writer.newLine();
            System.out.println("Log written: " + message);
        } catch (IOException e) {
            System.err.println("Failed to write log: " + e.getMessage());
        }
    }
}
