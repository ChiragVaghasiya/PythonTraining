from sqlalchemy import Column, Integer, Float, Date, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class MasterDetails(Base):
    __tablename__ = 'master_details'
    id = Column(Integer, primary_key=True, index=True)
    basic_details = relationship("BasicDetails", back_populates="master_details")
    tax_rebate = relationship("TaxRebate", back_populates="master_details")
    min_basic = relationship("MinBasic", back_populates="master_details")
    max_basic = relationship("MaxBasic", back_populates="master_details")
    old_regime_tax_slabs = relationship("OldRegimeTaxSlabs", back_populates="master_details")
    new_regime_tax_slabs = relationship("NewRegimeTaxSlabs", back_populates="master_details")
    old_regime_surcharge_slabs = relationship("OldRegimeSurchargeSlabs", back_populates="master_details")
    new_regime_surcharge_slabs = relationship("NewRegimeSurchargeSlabs", back_populates="master_details")

    name = Column(String(255))
    company_id = Column(String(255))
    date_from = Column(Date)
    date_to = Column(Date)


class BasicDetails(Base):
    __tablename__ = 'basic_details'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="basic_details")

    basic_percentage = Column(Float)
    hra = Column(Float)
    stan_ded_old_regime = Column(Integer)
    stan_ded_new_regime = Column(Integer)
    gratuity_percentage = Column(Float)
    gratuity_multiplier = Column(Float)
    cess = Column(Float)
    professional_tax = Column(Integer)
    physically_challenged = Column(Boolean, default=False)
    age_above = Column(Integer)
    monthly_salary_limit = Column(Integer)
    tax_deducted_at_source = Column(Float)
    pf_percentage = Column(Float)
    pf_ceiling_limit = Column(Float)
    esic_ee_percentage = Column(Float)
    esic_er_percentage = Column(Float)
    esic_wage_limit = Column(Float)
    esic_wag_lim_phy_cha = Column(Float)


class MinBasic(Base):
    __tablename__ = 'min_basic'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="min_basic")

    date_from = Column(Date)
    date_to = Column(Date)
    amount = Column(Float)


class MaxBasic(Base):
    __tablename__ = 'max_basic'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="max_basic")

    date_from = Column(Date)
    date_to = Column(Date)
    amount = Column(Float)


class TaxRebate(Base):
    __tablename__ = 'tax_rebate'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="tax_rebate")

    old_tax_nor_cit_reba_amo = Column(Float)
    old_tax_nor_cit_reba_inc = Column(Float)
    old_tax_sen_cit_reba_amo = Column(Float)
    old_tax_sen_cit_reba_inc = Column(Float)
    old_tax_sup_sen_cit_reba_amo = Column(Float)
    old_tax_sup_sen_cit_reba_inc = Column(Float)
    new_tax_nor_cit_reba_amo = Column(Float)
    new_tax_nor_cit_reba_inc = Column(Float)
    new_tax_sen_cit_reba_amo = Column(Float)
    new_tax_sen_cit_reba_inc = Column(Float)
    new_tax_sup_sen_cit_reba_amo = Column(Float)
    new_tax_sup_sen_cit_reba_inc = Column(Float)


class OldRegimeTaxSlabs(Base):
    __tablename__ = 'old_regime_tax_slabs'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="old_regime_tax_slabs")

    amount_from = Column(Integer)
    amount_to = Column(Integer)
    normal_citizen_percentage = Column(Float)
    senior_citizen_percentage = Column(Float)
    super_senior_citizen_percentage = Column(Float)


class NewRegimeTaxSlabs(Base):
    __tablename__ = 'new_regime_tax_slabs'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="new_regime_tax_slabs")

    amount_from = Column(Integer)
    amount_to = Column(Integer)
    normal_citizen_percentage = Column(Float)
    senior_citizen_percentage = Column(Float)
    super_senior_citizen_percentage = Column(Float)


class OldRegimeSurchargeSlabs(Base):
    __tablename__ = 'old_regime_surcharge_slabs'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="old_regime_surcharge_slabs")

    amount_from = Column(Integer)
    amount_to = Column(Integer)
    normal_citizen_percentage = Column(Float)
    senior_citizen_percentage = Column(Float)
    super_senior_citizen_percentage = Column(Float)


class NewRegimeSurchargeSlabs(Base):
    __tablename__ = 'new_regime_surcharge_slabs'
    id = Column(Integer, primary_key=True, index=True)
    master_details_id = Column(Integer, ForeignKey("master_details.id"))
    master_details = relationship("MasterDetails", back_populates="new_regime_surcharge_slabs")

    amount_from = Column(Integer)
    amount_to = Column(Integer)
    normal_citizen_percentage = Column(Float)
    senior_citizen_percentage = Column(Float)
    super_senior_citizen_percentage = Column(Float)
