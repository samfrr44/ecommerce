import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime
from sqlalchemy import Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry
from sqlalchemy import UniqueConstraint


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(30), unique = True)
    description: Mapped[str]
    products: Mapped[List["Product"]] = relationship(
        back_populates="category", lazy=True
    )

    def __repr__(self) -> str:
        return f"category(id={self.id!r}, name={self.name!r}, description={self.description!r})"


class Supplier(Base):
    __tablename__ = "supplier"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(30), unique = True)
    address: Mapped[str]
    city: Mapped[str]
    zipcode: Mapped[str] = mapped_column(Integer)
    country: Mapped[str]
    phone: Mapped[str]
    products: Mapped[List["Product"]] = relationship(
        back_populates="supplier", lazy=True
    )

    def __repr__(self) -> str:
        return f"supplier(id={self.id!r}, name={self.name!r}, address={self.address!r}, city={self.city!r}, zipcode={self.zipcode!r}, country={self.country!r}, phone={self.phone!r})"


class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str]
    city: Mapped[str]
    zipcode: Mapped[str] = mapped_column(Integer)
    country: Mapped[str]
    phone: Mapped[str]
    orders: Mapped[List["Order"]] = relationship(
        back_populates="customer", lazy=True
    )

    def __repr__(self) -> str:
        return f"customer(id={self.id!r}, name={self.name!r}, address={self.address!r}, city={self.city!r}, zipcode={self.zipcode!r}, country={self.country!r}, phone={self.phone!r})"


class Order(Base):
    __tablename__ = "order"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    date: Mapped[str] = mapped_column(DateTime)
    customer_id: Mapped[UUID(as_uuid=True)] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    orderItems: Mapped[List["OrderItem"]] = relationship(
        back_populates="order", lazy=True
    )

    def __repr__(self) -> str:
        return f"order(id={self.id!r}, name={self.name!r}, date={self.date!r})"


class Product(Base):
    __tablename__ = "product"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(unique=True)
    unit: Mapped[str]
    price: Mapped[str] = mapped_column(Float)
    category_id: Mapped[UUID(as_uuid=True)] = mapped_column(ForeignKey("category.id"))
    supplier_id: Mapped[UUID(as_uuid=True)] = mapped_column(ForeignKey("supplier.id"))
    category: Mapped["Category"] = relationship(back_populates="products")
    supplier: Mapped["Supplier"] = relationship(back_populates="products")
    orderItems: Mapped[List["OrderItem"]] = relationship(
        back_populates="product", lazy=True
    )

    def __repr__(self) -> str:
        return f"product(id={self.id!r}, name={self.name!r}, unit={self.name!r}, price={self.name!r})"


class OrderItem(Base):
    __tablename__ = "order_item"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    quantity: Mapped[str] = mapped_column(Integer)
    order_id: Mapped[UUID(as_uuid=True)] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[UUID(as_uuid=True)] = mapped_column(ForeignKey("product.id"))
    order: Mapped["Order"] = relationship(back_populates="orderItems")
    product: Mapped["Product"] = relationship(back_populates="orderItems")
    UniqueConstraint("order_id", "product_id", name="uix_orderproduct")
    def __repr__(self) -> str:
        return f"product(id={self.id!r}, quantity={self.quantity!r})"
