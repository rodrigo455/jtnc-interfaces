AC_INIT(freqrefInterfaces,  1.0.3)

AM_INIT_AUTOMAKE(nostdinc)
AC_PROG_CC
AC_PROG_CXX
AC_PROG_INSTALL
AC_PROG_LIBTOOL

AM_PATH_PYTHON([2.3])

OSSIE_CHECK_OSSIE
OSSIE_OSSIEHOME_AS_PREFIX
OSSIE_PYTHON_INSTALL_SCHEME

AC_CORBA_ORB
AC_CHECK_PROG([IDL], [omniidl], [omniidl], [no])
if test "$IDL" = no; then
  AC_MSG_ERROR([cannot find omniidl program])
fi
AC_LANG_PUSH([C++])
PKG_CHECK_MODULES([OMNIORB], [omniORB4 >= 4.1.0])
PKG_CHECK_MODULES([OSSIE], [ossie >= 2.1.0])

# If you depend on other IDL modules, such as CF or BULKIO add them here
# PKG_CHECK_MODULES([BULKIO], [bulkioInterfaces >= 2.1.0])
# AC_CHECK_PYMODULE(bulkio.bulkioInterfaces, [], [AC_MSG_ERROR([the python bulkio.bulkioInterfaces module is required])])

# Optionally include java support
AC_ARG_ENABLE([java], AS_HELP_STRING([--disable-java], [Disable framework java support]))

HAVE_JAVASUPPORT=no
if test "x$enable_java" != "xno"; then
  # Ensure JAVA_HOME is set
  AC_ARG_VAR([JAVA_HOME], [Java Development Kit (JDK) location])
  test -r /usr/share/java-utils/java-functions && \
    . /usr/share/java-utils/java-functions && \
    set_jvm
  AC_MSG_CHECKING([for a valid JAVA_HOME])
  if test -n "$JAVA_HOME" -a -d "$JAVA_HOME"; then
    AC_MSG_RESULT([$JAVA_HOME])
    java_test_paths=$JAVA_HOME/jre/sh$PATH_SEPARATOR$JAVA_HOME/bin$PATH_SEPARATOR$PATH
  else
    AC_MSG_RESULT([no - this may impact Java tool detection])
    java_test_paths=$PATH
  fi

  # Locate tools we need
  AC_PATH_PROG([JAVAC], [javac], [no], [$java_test_paths])
  AC_PATH_PROG([JAR], [jar], [no], [$java_test_paths])
  AC_PATH_PROG([IDLJ], [idlj], [no], [$java_test_paths])
  AS_IF([test "$JAVAC" = no -o "$JAR" = no -o "$IDLJ" = no],
        [AC_MSG_ERROR([Cannot find a required Java tool])])

  HAVE_JAVASUPPORT=yes
fi
AM_CONDITIONAL(HAVE_JAVASUPPORT, test $HAVE_JAVASUPPORT = yes)

AC_CONFIG_FILES(Makefile)
AC_OUTPUT
