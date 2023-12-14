BUILD_DIR := ./build

SRCS := $(shell find . -name '*.py')
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

ROBOT_NAME := "zeus"

build: $(OBJS)
	@echo "Building"

$(BUILD_DIR)/%.py.o: %.py
	./upload.sh $(ROBOT_NAME) $<
	@mkdir -p $(dir $@)
	@touch $@