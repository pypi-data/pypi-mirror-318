#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* mfnsetup.c */
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

#include "slepcmfn.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsetup_ MFNSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetup_ mfnsetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsetoperator_ MFNSETOPERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetoperator_ mfnsetoperator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetoperator_ MFNGETOPERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetoperator_ mfngetoperator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnallocatesolution_ MFNALLOCATESOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnallocatesolution_ mfnallocatesolution
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  mfnsetup_(MFN mfn, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNSetUp(
	(MFN)PetscToPointer((mfn) ));
}
SLEPC_EXTERN void  mfnsetoperator_(MFN mfn,Mat A, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(A);
*ierr = MFNSetOperator(
	(MFN)PetscToPointer((mfn) ),
	(Mat)PetscToPointer((A) ));
}
SLEPC_EXTERN void  mfngetoperator_(MFN mfn,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = MFNGetOperator(
	(MFN)PetscToPointer((mfn) ),A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  mfnallocatesolution_(MFN mfn,PetscInt *extra, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNAllocateSolution(
	(MFN)PetscToPointer((mfn) ),*extra);
}
#if defined(__cplusplus)
}
#endif
