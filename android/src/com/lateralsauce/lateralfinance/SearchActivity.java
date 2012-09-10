package com.lateralsauce.lateralfinance;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;

import android.app.Activity;
import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.AutoCompleteTextView;
import android.widget.BaseAdapter;
import android.widget.Filter;
import android.widget.Filterable;
import android.widget.TextView;

import com.googlecode.androidannotations.annotations.AfterViews;
import com.googlecode.androidannotations.annotations.EActivity;
import com.googlecode.androidannotations.annotations.ViewById;

@EActivity(R.layout.search)
public class SearchActivity extends Activity {

	@ViewById
	AutoCompleteTextView autocomplete;

	@AfterViews
	void setUpAutocomplete() {
		final AutocompleteAdapter adapter = new AutocompleteAdapter(this);
		autocomplete.setAdapter(adapter);
		autocomplete.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
				autocompleteItemClicked(adapter.getItem(position));
			}
		});
	}

	void autocompleteItemClicked(Company company) {
		QuoteActivity_.intent(this).company(company).start();
		autocomplete.setText("");
	}
}

class AutocompleteAdapter extends BaseAdapter implements Filterable {

	private List<Company> companies = Collections.emptyList();
	private ServerFilter filter;
	private Context context;

	public AutocompleteAdapter(Context context) {
		this.context = context;
	}

	@Override
	public int getCount() {
		return companies.size();
	}

	@Override
	public Company getItem(int position) {
		return companies.get(position);
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {

		TextView textView;
		if (convertView == null) {
			textView = (TextView) View.inflate(context, android.R.layout.simple_dropdown_item_1line, null);
		} else {
			textView = (TextView) convertView;
		}
		Company company = getItem(position);

		textView.setText(company.getDisplayName());

		return textView;
	}

	@Override
	public Filter getFilter() {
		if (filter == null) {
			filter = new ServerFilter(this);
		}
		return filter;
	}

	public void updateCompanies(List<Company> companies) {
		this.companies = companies;
		notifyDataSetChanged();
	}
}

class ServerFilter extends Filter {

	private List<Company> allCompanies;
	private String lastConstraint;
	private final AutocompleteAdapter adapter;

	public ServerFilter(AutocompleteAdapter adapter) {
		this.adapter = adapter;
	}

	@Override
	protected FilterResults performFiltering(CharSequence constraint) {
		final FilterResults filterResults = new FilterResults();

		if (constraint == null) {
			filterResults.count = 0;
			filterResults.values = Collections.emptyList();
			return filterResults;
		}

		String dataConstraint = constraint.toString();
		if (lastConstraint != null && constraint.toString().startsWith(lastConstraint)) {
			final List<Company> results = filterData(allCompanies, dataConstraint);
			filterResults.values = results;
			filterResults.count = results.size();
		} else {
			allCompanies = getDataFromServer(constraint);
			filterResults.values = allCompanies;
			filterResults.count = allCompanies.size();
			lastConstraint = dataConstraint;
		}
		return filterResults;
	}

	private List<Company> filterData(final List<Company> fullData, final String constraint) {
		final List<Company> results = new ArrayList<Company>();
		for (Company company : fullData) {
			if (company.getName().toLowerCase().startsWith(constraint.toLowerCase())) {
				results.add(company);
			}
		}
		return results;
	}

	private List<Company> getDataFromServer(CharSequence constraint) {
		final String URL = "http://192.168.1.46:8000/search?q=" + constraint.toString();
		HttpClient httpclient = new DefaultHttpClient();
		try {
			HttpResponse response = httpclient.execute(new HttpGet(URL));
			StatusLine statusLine = response.getStatusLine();
			if (statusLine.getStatusCode() == HttpStatus.SC_OK) {
				ByteArrayOutputStream out = new ByteArrayOutputStream();
				response.getEntity().writeTo(out);
				out.close();
				String responseString = out.toString();
				JSONArray jsonArray = new JSONArray(responseString);
				List<Company> companies = new ArrayList<Company>(jsonArray.length());
				for (int i = 0; i < jsonArray.length(); i++) {
					companies.add(new Company(jsonArray.getJSONObject(i)));
				}
				return companies;
			} else {
				// Closes the connection.
				response.getEntity().getContent().close();
				throw new IOException(statusLine.getReasonPhrase());
			}
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	@Override
	protected void publishResults(CharSequence constraint, FilterResults results) {
		@SuppressWarnings("unchecked")
		List<Company> filteredCompanies = (List<Company>) results.values;
		adapter.updateCompanies(filteredCompanies);
	}

}