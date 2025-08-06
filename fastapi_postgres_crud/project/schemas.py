from datetime import date
from typing import List

from pydantic import BaseModel


# -------------------------------
# MinBasic Schemas
# -------------------------------
class MinBasicBase(BaseModel):
    master_details_id: int
    date_from: date
    date_to: date
    amount: float


class MinBasicCreate(MinBasicBase):
    pass


class MinBasicRead(MinBasicBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# MaxBasic Schemas
# -------------------------------
class MaxBasicBase(BaseModel):
    master_details_id: int
    date_from: date
    date_to: date
    amount: float


class MaxBasicCreate(MaxBasicBase):
    pass


class MaxBasicRead(MaxBasicBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# OldRegimeTaxSlabs Schemas
# -------------------------------
class OldRegimeTaxSlabsBase(BaseModel):
    master_details_id: int
    amount_from: int
    amount_to: int
    normal_citizen_percentage: float
    senior_citizen_percentage: float
    super_senior_citizen_percentage: float


class OldRegimeTaxSlabsCreate(OldRegimeTaxSlabsBase):
    pass


class OldRegimeTaxSlabsRead(OldRegimeTaxSlabsBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# NewRegimeTaxSlabs Schemas
# -------------------------------
class NewRegimeTaxSlabsBase(BaseModel):
    master_details_id: int
    amount_from: int
    amount_to: int
    normal_citizen_percentage: float
    senior_citizen_percentage: float
    super_senior_citizen_percentage: float


class NewRegimeTaxSlabsCreate(NewRegimeTaxSlabsBase):
    pass


class NewRegimeTaxSlabsRead(NewRegimeTaxSlabsBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# OldRegimeSurchargeSlabs Schemas
# -------------------------------
class OldRegimeSurchargeSlabsBase(BaseModel):
    master_details_id: int
    amount_from: int
    amount_to: int
    normal_citizen_percentage: float
    senior_citizen_percentage: float
    super_senior_citizen_percentage: float


class OldRegimeSurchargeSlabsCreate(OldRegimeSurchargeSlabsBase):
    pass


class OldRegimeSurchargeSlabsRead(OldRegimeSurchargeSlabsBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# NewRegimeSurchargeSlabs Schemas
# -------------------------------
class NewRegimeSurchargeSlabsBase(BaseModel):
    master_details_id: int
    amount_from: int
    amount_to: int
    normal_citizen_percentage: float
    senior_citizen_percentage: float
    super_senior_citizen_percentage: float


class NewRegimeSurchargeSlabsCreate(NewRegimeSurchargeSlabsBase):
    pass


class NewRegimeSurchargeSlabsRead(NewRegimeSurchargeSlabsBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# TaxRebate Schemas
# -------------------------------
class TaxRebateBase(BaseModel):
    master_details_id: int
    old_tax_nor_cit_reba_amo: float
    old_tax_nor_cit_reba_inc: float
    old_tax_sen_cit_reba_amo: float
    old_tax_sen_cit_reba_inc: float
    old_tax_sup_sen_cit_reba_amo: float
    old_tax_sup_sen_cit_reba_inc: float
    new_tax_nor_cit_reba_amo: float
    new_tax_nor_cit_reba_inc: float
    new_tax_sen_cit_reba_amo: float
    new_tax_sen_cit_reba_inc: float
    new_tax_sup_sen_cit_reba_amo: float
    new_tax_sup_sen_cit_reba_inc: float


class TaxRebateCreate(TaxRebateBase):
    pass


class TaxRebateRead(TaxRebateBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# BasicDetails Schemas
# -------------------------------
class BasicDetailsBase(BaseModel):
    master_details_id: int
    basic_percentage: float
    hra: float
    stan_ded_old_regime: int
    stan_ded_new_regime: int
    gratuity_percentage: float
    gratuity_multiplier: float
    cess: float
    professional_tax: int
    physically_challenged: bool
    age_above: int
    monthly_salary_limit: int
    tax_deducted_at_source: float
    pf_percentage: float
    pf_ceiling_limit: float
    esic_ee_percentage: float
    esic_er_percentage: float
    esic_wage_limit: float
    esic_wag_lim_phy_cha: float


class BasicDetailsCreate(BasicDetailsBase):
    pass


class BasicDetailsRead(BasicDetailsBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------------
# MasterDetails Schemas
# -------------------------------
class MasterDetailsBase(BaseModel):
    name: str
    company_id: str
    date_from: date
    date_to: date


class MasterDetailsCreate(MasterDetailsBase):
    pass


class MasterDetailsRead(MasterDetailsBase):
    id: int
    basic_details: List[BasicDetailsRead] = []
    tax_rebate: List[TaxRebateRead] = []
    min_basic: List[MinBasicRead] = []
    max_basic: List[MaxBasicRead] = []
    old_regime_tax_slabs: List[OldRegimeTaxSlabsRead] = []
    new_regime_tax_slabs: List[NewRegimeTaxSlabsRead] = []
    old_regime_surcharge_slabs: List[OldRegimeSurchargeSlabsRead] = []
    new_regime_surcharge_slabs: List[NewRegimeSurchargeSlabsRead] = []

    class Config:
        orm_mode = True
