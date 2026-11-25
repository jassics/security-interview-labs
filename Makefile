.PHONY: test clean

test:
	$(MAKE) -C product-security test

clean:
	$(MAKE) -C product-security clean
