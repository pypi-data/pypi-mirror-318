#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* mfnsolve.c */
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
#define mfnsolve_ MFNSOLVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsolve_ mfnsolve
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsolvetranspose_ MFNSOLVETRANSPOSE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsolvetranspose_ mfnsolvetranspose
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetiterationnumber_ MFNGETITERATIONNUMBER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetiterationnumber_ mfngetiterationnumber
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetconvergedreason_ MFNGETCONVERGEDREASON
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetconvergedreason_ mfngetconvergedreason
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  mfnsolve_(MFN mfn,Vec b,Vec x, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(b);
CHKFORTRANNULLOBJECT(x);
*ierr = MFNSolve(
	(MFN)PetscToPointer((mfn) ),
	(Vec)PetscToPointer((b) ),
	(Vec)PetscToPointer((x) ));
}
SLEPC_EXTERN void  mfnsolvetranspose_(MFN mfn,Vec b,Vec x, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(b);
CHKFORTRANNULLOBJECT(x);
*ierr = MFNSolveTranspose(
	(MFN)PetscToPointer((mfn) ),
	(Vec)PetscToPointer((b) ),
	(Vec)PetscToPointer((x) ));
}
SLEPC_EXTERN void  mfngetiterationnumber_(MFN mfn,PetscInt *its, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLINTEGER(its);
*ierr = MFNGetIterationNumber(
	(MFN)PetscToPointer((mfn) ),its);
}
SLEPC_EXTERN void  mfngetconvergedreason_(MFN mfn,MFNConvergedReason *reason, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNGetConvergedReason(
	(MFN)PetscToPointer((mfn) ),reason);
}
#if defined(__cplusplus)
}
#endif
