package app.lab2;

import java.lang.reflect.Array;
import java.util.List;
import java.util.Map;

public record SubmitRequest(List<Map<String, Double>> pairs, Float x) {}
