# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/bn.h>
"""

TYPES = """
typedef ... BN_CTX;
typedef ... BN_MONT_CTX;
typedef ... BIGNUM;
typedef int... BN_ULONG;
"""

FUNCTIONS = """
#define BN_FLG_CONSTTIME ...

void BN_set_flags(BIGNUM *, int);
int BN_get_flags(const BIGNUM *, int);

BIGNUM *BN_new(void);
void BN_free(BIGNUM *);
void BN_clear_free(BIGNUM *);

int BN_rand(BIGNUM *, int, int, int);
int BN_rand_range(BIGNUM *, BIGNUM *);

BN_CTX *BN_CTX_new(void);
void BN_CTX_free(BN_CTX *);

void BN_CTX_start(BN_CTX *);
BIGNUM *BN_CTX_get(BN_CTX *);
void BN_CTX_end(BN_CTX *);

BN_MONT_CTX *BN_MONT_CTX_new(void);
int BN_MONT_CTX_set(BN_MONT_CTX *, BIGNUM *, BN_CTX *);
void BN_MONT_CTX_free(BN_MONT_CTX *);

BIGNUM *BN_copy(BIGNUM *, const BIGNUM *);
BIGNUM *BN_dup(const BIGNUM *);

int BN_set_word(BIGNUM *, BN_ULONG);
BN_ULONG BN_get_word(const BIGNUM *);

const BIGNUM *BN_value_one(void);

char *BN_bn2hex(const BIGNUM *);
int BN_hex2bn(BIGNUM **, const char *);
int BN_dec2bn(BIGNUM **, const char *);

int BN_bn2bin(const BIGNUM *, unsigned char *);
BIGNUM *BN_bin2bn(const unsigned char *, int, BIGNUM *);

int BN_num_bits(const BIGNUM *);

int BN_cmp(const BIGNUM *, const BIGNUM *);
int BN_add(BIGNUM *, const BIGNUM *, const BIGNUM *);
int BN_sub(BIGNUM *, const BIGNUM *, const BIGNUM *);
int BN_mul(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);
int BN_sqr(BIGNUM *, const BIGNUM *, BN_CTX *);
int BN_div(BIGNUM *, BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);
int BN_nnmod(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);
int BN_mod_add(BIGNUM *, const BIGNUM *, const BIGNUM *, const BIGNUM *,
               BN_CTX *);
int BN_mod_sub(BIGNUM *, const BIGNUM *, const BIGNUM *, const BIGNUM *,
               BN_CTX *);
int BN_mod_mul(BIGNUM *, const BIGNUM *, const BIGNUM *, const BIGNUM *,
               BN_CTX *);
int BN_mod_sqr(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);
int BN_exp(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);
int BN_mod_exp(BIGNUM *, const BIGNUM *, const BIGNUM *, const BIGNUM *,
               BN_CTX *);
int BN_mod_exp_mont(BIGNUM *, const BIGNUM *, const BIGNUM *, const BIGNUM *,
                    BN_CTX *, BN_MONT_CTX *);
int BN_mod_exp_mont_consttime(BIGNUM *, const BIGNUM *, const BIGNUM *,
                              const BIGNUM *, BN_CTX *, BN_MONT_CTX *);
int BN_gcd(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);
BIGNUM *BN_mod_inverse(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);

int BN_set_bit(BIGNUM *, int);
int BN_clear_bit(BIGNUM *, int);

int BN_is_bit_set(const BIGNUM *, int);

int BN_mask_bits(BIGNUM *, int);

int BN_num_bytes(const BIGNUM *);

int BN_zero(BIGNUM *);
int BN_one(BIGNUM *);
int BN_mod(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);

int BN_lshift(BIGNUM *, const BIGNUM *, int);
int BN_lshift1(BIGNUM *, BIGNUM *);

int BN_rshift(BIGNUM *, BIGNUM *, int);
int BN_rshift1(BIGNUM *, BIGNUM *);
"""

CUSTOMIZATIONS = """
"""
