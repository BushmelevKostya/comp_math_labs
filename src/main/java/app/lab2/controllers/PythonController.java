package app.lab2.controllers;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;
import java.util.List;
import java.util.Map;

@RestController
public class PythonController {
	@CrossOrigin(origins = "http://localhost:8080")
	@PostMapping("api/run-python-script")
	public String runPythonScript(@RequestBody String pairs) {
		try {
			String currentDir = System.getProperty("user.dir");
			String scriptPath;
			String launchCommand;
			String osName = System.getProperty("os.name").toLowerCase();
			if (osName.contains("windows")) {
				scriptPath = currentDir + "\\src\\main\\resources\\scripts\\main.py";
				launchCommand = "python";
			} else {
				scriptPath = currentDir + "/back/test.py";
				launchCommand = "python3";
			}
			ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, pairs);
			Process process = processBuilder.start();
			
			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
			StringBuilder output = new StringBuilder();
			String line;
			while ((line = reader.readLine()) != null) {
				output.append(line).append("\n");
			}
			StringBuilder errorOutput = new StringBuilder();
			while ((line = errorReader.readLine()) != null) {
				errorOutput.append(line).append("\n");
			}
			if (!errorOutput.toString().equals("")) System.out.println("Error executing Python script. Error output: " + errorOutput.toString());
			return output.toString();
			
		} catch (IOException e) {
			System.out.println(System.getProperty("user.dir"));
			return "Error executing Python script";
		}
	}
}
