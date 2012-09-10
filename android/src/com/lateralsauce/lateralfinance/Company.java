package com.lateralsauce.lateralfinance;

import java.io.Serializable;
import java.util.Arrays;
import java.util.List;

import org.json.JSONException;
import org.json.JSONObject;

public class Company implements Serializable {

	private static final long serialVersionUID = 1L;

	private String name;
	private String symbol;
	private String market;
	private String currency;

	public static List<Company> getFakeData() {
		return Arrays.asList(new Company("Illiad", "ILA", "Paris", "EUR"), new Company("Illogique", "IBD", "Paris", "EUR"), new Company("Illationel", "ILC", "Paris", "EUR"), new Company("Illegitime", "ILD", "Paris", "EUR"), new Company("Illalalacafaitmal", "ILD", "Paris", "EUR"), new Company("Illiade", "OLALA", "Paris", "EUR"), new Company("Illiud", "ILAD", "Paris", "EUR"), new Company("Illied", "ILAA", "Paris", "EUR"));
	}

	public Company() {
	}

	public Company(JSONObject jsonObject) {
		try {
			name = jsonObject.getString("name");
			symbol = jsonObject.getString("symbol");
			currency = jsonObject.getString("currency");
			market = jsonObject.getString("market");
		} catch (JSONException e) {
			throw new IllegalArgumentException();
		}
	}

	public Company(String name, String symbol, String market, String currency) {
		this.name = name;
		this.symbol = symbol;
		this.market = market;
		this.currency = currency;
	}

	public String getDisplayName() {
		return name + " (" + symbol + ")";
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSymbol() {
		return symbol;
	}

	public void setSymbol(String symbol) {
		this.symbol = symbol;
	}

	public String getMarket() {
		return market;
	}

	public void setMarket(String market) {
		this.market = market;
	}

	public String getCurrency() {
		return currency;
	}

	public void setCurrency(String currency) {
		this.currency = currency;
	}

	@Override
	public String toString() {
		return getDisplayName();
	}
}
