#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring

JNICALL
Java_com_example_tanermetin_commudp_1ndk_MainActivity_stringFromJNI(
        JNIEnv *env,
        jobject /* this */) {
    std::string hello = "Hello from native-lib.cpp";
    return env->NewStringUTF(hello.c_str());
}
