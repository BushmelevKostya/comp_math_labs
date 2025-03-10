package app.lab2.controllers;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;

@RestController
public class PythonController {
	@CrossOrigin(origins = "http://localhost:8080")
	@PostMapping("api/run-python-script")
	public String runPythonScript(@RequestParam("lbname") String lbname, @RequestParam("type") String type,
	                              @RequestParam("quation") String quation, @RequestParam("method") String method,
	                              @RequestParam("leftBorder") String leftBorder, @RequestParam("rightBorder") String rightBorder,
	                              @RequestParam("inaccuary") String inaccuary,  @RequestParam("answer") String answer,
	                              @RequestParam("filepath") String filepath) {
		try {
			System.out.println(lbname + " " + type + " " + quation + " " + method + " " + leftBorder + " " + rightBorder + " " + inaccuary);
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
			ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, type, quation, method, leftBorder, rightBorder, inaccuary, answer, filepath);
			Process process = processBuilder.start();
			
			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			StringBuilder output = new StringBuilder();
			String line;
			while ((line = reader.readLine()) != null) {
				output.append(line).append("\n");
			}
			
			int exitCode = process.waitFor();
			System.out.println(output);
//			System.out.println(scriptPath);
			return output.toString();
			
		} catch (IOException | InterruptedException e) {
			System.out.println(System.getProperty("user.dir"));
			return "Error executing Python script";
		}
	}
}
