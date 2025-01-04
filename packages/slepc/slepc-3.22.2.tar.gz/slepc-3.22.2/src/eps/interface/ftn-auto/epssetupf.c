#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* epssetup.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetdstype_ EPSSETDSTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetdstype_ epssetdstype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetup_ EPSSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetup_ epssetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetoperators_ EPSSETOPERATORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetoperators_ epssetoperators
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgetoperators_ EPSGETOPERATORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgetoperators_ epsgetoperators
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetdeflationspace_ EPSSETDEFLATIONSPACE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetdeflationspace_ epssetdeflationspace
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetinitialspace_ EPSSETINITIALSPACE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetinitialspace_ epssetinitialspace
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetleftinitialspace_ EPSSETLEFTINITIALSPACE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetleftinitialspace_ epssetleftinitialspace
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsallocatesolution_ EPSALLOCATESOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsallocatesolution_ epsallocatesolution
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epssetdstype_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSSetDSType(
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  epssetup_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSSetUp(
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  epssetoperators_(EPS eps,Mat A,Mat B, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
*ierr = EPSSetOperators(
	(EPS)PetscToPointer((eps) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ));
}
SLEPC_EXTERN void  epsgetoperators_(EPS eps,Mat *A,Mat *B, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool B_null = !*(void**) B ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(B);
*ierr = EPSGetOperators(
	(EPS)PetscToPointer((eps) ),A,B);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! B_null && !*(void**) B) * (void **) B = (void *)-2;
}
SLEPC_EXTERN void  epssetdeflationspace_(EPS eps,PetscInt *n,Vec v[], int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = EPSSetDeflationSpace(
	(EPS)PetscToPointer((eps) ),*n,v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  epssetinitialspace_(EPS eps,PetscInt *n,Vec is[], int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool is_null = !*(void**) is ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(is);
*ierr = EPSSetInitialSpace(
	(EPS)PetscToPointer((eps) ),*n,is);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! is_null && !*(void**) is) * (void **) is = (void *)-2;
}
SLEPC_EXTERN void  epssetleftinitialspace_(EPS eps,PetscInt *n,Vec isl[], int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool isl_null = !*(void**) isl ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(isl);
*ierr = EPSSetLeftInitialSpace(
	(EPS)PetscToPointer((eps) ),*n,isl);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! isl_null && !*(void**) isl) * (void **) isl = (void *)-2;
}
SLEPC_EXTERN void  epsallocatesolution_(EPS eps,PetscInt *extra, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSAllocateSolution(
	(EPS)PetscToPointer((eps) ),*extra);
}
#if defined(__cplusplus)
}
#endif
