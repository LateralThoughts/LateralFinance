package com.lateralsauce.lateralfinance;

import android.app.Activity;
import android.widget.TextView;

import com.googlecode.androidannotations.annotations.AfterViews;
import com.googlecode.androidannotations.annotations.EActivity;
import com.googlecode.androidannotations.annotations.Extra;
import com.googlecode.androidannotations.annotations.ViewById;

@EActivity(R.layout.quote)
public class QuoteActivity extends Activity {

	@Extra
	Company company;

	@ViewById
	TextView companyName;

	@AfterViews
	void setUpData() {
		companyName.setText(company.getDisplayName());
	}
}
