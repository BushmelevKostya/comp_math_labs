package app.lab2.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;

@RestController
public class PythonController {
	
	@GetMapping("api/run-python-script")
	public String runPythonScript(@RequestParam("lbname") String lbname, @RequestParam("type") String type,
	                              @RequestParam("quation") String quation, @RequestParam("method") String method,
	                              @RequestParam("leftBorder") String leftBorder, @RequestParam("rightBorder") String rightBorder,
	                              @RequestParam("inaccuary") String inaccuary) {
		try {
			System.out.println(lbname + " " + type + " " + quation + " " + method + " " + leftBorder + " " + rightBorder + " " + inaccuary);
			String currentDir = System.getProperty("user.dir");
			String scriptPath;
			String launchCommand;
			String osName = System.getProperty("os.name").toLowerCase();
			if (osName.contains("windows")) {
				scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb2\\main.py";
				launchCommand = "python";
			} else {
				scriptPath = currentDir + "/back/test.py";
				launchCommand = "python3";
			}
			ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, type, quation, method, leftBorder, rightBorder, inaccuary);
			Process process = processBuilder.start();
			
			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			StringBuilder output = new StringBuilder();
			String line;
			while ((line = reader.readLine()) != null) {
				output.append(line).append("\n");
			}
			
			int exitCode = process.waitFor();
			System.out.println(output.toString());
			System.out.println(scriptPath);
			return output.toString();
			
		} catch (IOException | InterruptedException e) {
			System.out.println(System.getProperty("user.dir"));
			return "Error executing Python script";
		}
	}
	
//	@PostMapping("/api/send-file")
//	public String handleFileUpload(@RequestParam("file") MultipartFile file) {
//		if (!file.isEmpty()) {
//			try {
//				// Читаем содержимое файла в строку
//				String fileContent = new String(file.getBytes());
//				String[] lines = fileContent.split("\\n");
//				// Выводим содержимое файла на сервере
//				System.out.println("File context");
//				for (String line : lines) {
//					System.out.println(line);
//				}
//				ValidateFile validator = new ValidateFile();
//				boolean isValid = validator.validateFile(lines);
//
//				if (!isValid) {
//					return "Uncorrected file.";
//				}
//
//				String currentDir = System.getProperty("user.dir");
//				String scriptPath;
//				String launchCommand;
//				String osName = System.getProperty("os.name").toLowerCase();
//				if (osName.contains("windows")) {
//					scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb2\\main.py";
//					launchCommand = "python";
//				} else {
//					scriptPath = currentDir + "/back/test.py";
//					launchCommand = "python3";
//				}
//				///root/back/test.py
//				// Создаем объект ProcessBuilder для запуска Python скрипта
//				ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]);
//				// Запускаем процесс
//				Process process = processBuilder.start();
//
//				// Читаем вывод скрипта
//				BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
//				StringBuilder output = new StringBuilder();
//				String line;
//				while ((line = reader.readLine()) != null) {
//					output.append(line).append("\n");
//				}
//
//				// Ждем завершения процесса и получаем его код возврата
//				int exitCode = process.waitFor();
//				System.out.println(output.toString());
//				System.out.println(scriptPath);
//				// Возвращаем результат выполнения скрипта и его код возврата
//				return output.toString();
//			} catch (IOException e) {
//				return "Ошибка при чтении файла: " + e.getMessage();
//			} catch (InterruptedException e) {
//				throw new RuntimeException(e);
//			}
//		} else {
//			return "Choose the file";
//		}
//	}
}