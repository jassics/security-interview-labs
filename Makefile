.PHONY: test clean

test:
	$(MAKE) -C product-security test
	$(MAKE) test-market-data

clean:
	$(MAKE) -C product-security clean

.PHONY: test-market-data
test-market-data:
	cd market-data && python3 -m pytest -q
