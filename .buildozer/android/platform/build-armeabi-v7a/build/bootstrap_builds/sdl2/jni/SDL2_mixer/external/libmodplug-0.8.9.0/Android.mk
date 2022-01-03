LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := modplug

LOCAL_C_INCLUDES := $(LOCAL_PATH)/src $(LOCAL_PATH)/src/libmodplug 

LOCAL_CFLAGS += -DHAVE_SETENV -DHAVE_SINF

LOCAL_SRC_FILES += \
    src/fastmix.cpp \
    src/load_669.cpp \
    src/load_abc.cpp \
    src/load_amf.cpp \
    src/load_ams.cpp \
    src/load_dbm.cpp \
    src/load_dmf.cpp \
    src/load_dsm.cpp \
    src/load_far.cpp \
    src/load_it.cpp \
    src/load_j2b.cpp \
    src/load_mdl.cpp \
    src/load_med.cpp \
    src/load_mid.cpp \
    src/load_mod.cpp \
    src/load_mt2.cpp \
    src/load_mtm.cpp \
    src/load_okt.cpp \
    src/load_pat.cpp \
    src/load_psm.cpp \
    src/load_ptm.cpp \
    src/load_s3m.cpp \
    src/load_stm.cpp \
    src/load_ult.cpp \
    src/load_umx.cpp \
    src/load_wav.cpp \
    src/load_xm.cpp \
    src/mmcmp.cpp \
    src/modplug.cpp \
    src/snd_dsp.cpp \
    src/snd_flt.cpp \
    src/snd_fx.cpp \
    src/sndfile.cpp \
    src/sndmix.cpp

include $(BUILD_STATIC_LIBRARY)
