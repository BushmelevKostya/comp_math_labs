package app.lab2.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloWorldController {
	
	@GetMapping("/hello")
	@ResponseBody
	public String helloWorld() {
		return "Hello, World!";
	}
}