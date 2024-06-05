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

import java.util.List;
import java.util.Map;

@SpringBootApplication
@RestController
public class Lab2Application {
	
	public static void main(String[] args) {
		SpringApplication.run(Lab2Application.class, args);
	}
	
	@CrossOrigin(origins = "http://localhost:3000")
	@PostMapping("/submit")
	public String submit(@RequestBody SubmitRequest request) {
		System.out.println(request);
		List<Float> floatList = request.floatValues();
		Integer n = request.intValue();
		String func = request.selectedFunc();

		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_JSON);
		MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
		map.add("floatList", floatList.toString());
		if (n != null) {
			map.add("n", n.toString());
		} else {
			map.add("n", "0");
		}
		if (func != null){
			map.add("func", func);
		}
//		System.out.println(pairs);
		
		HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);

		String url = "http://localhost:8080/api/run-python-script";

		RestTemplate restTemplate = new RestTemplate();

		return restTemplate.exchange(url, HttpMethod.POST, entity, String.class).getBody();
	}
}
