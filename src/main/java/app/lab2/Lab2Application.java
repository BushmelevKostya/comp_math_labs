package app.lab2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
@RestController
public class Lab2Application {
	
	public static void main(String[] args) {
		SpringApplication.run(Lab2Application.class, args);
	}
	
	@CrossOrigin(origins = "http://localhost:3000")
	@PostMapping("/submit")
	public String submit(@RequestBody SubmitRequest request) {
		String a = request.intervalA();
		String b = request.intervalB();
		String gNum = String.valueOf(request.graphNumber());
		String mNum = String.valueOf(request.methodNumber());
		String error = String.valueOf(request.error());
		String answer = request.answer();
		String filepath = request.filepath();

		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

		MultiValueMap<String, String> map= new LinkedMultiValueMap<>();
		map.add("lbname", "value");
		map.add("type", "true");
		map.add("quation", gNum);
		map.add("method", mNum);
		map.add("leftBorder", a);
		map.add("rightBorder", b);
		map.add("inaccuary", error);
		map.add("answer", answer);
		map.add("filepath", filepath);

		HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);

		String url = "http://localhost:8080/api/run-python-script";

		RestTemplate restTemplate = new RestTemplate();

		return restTemplate.exchange(url, HttpMethod.POST, entity, String.class).getBody();
	}
}
