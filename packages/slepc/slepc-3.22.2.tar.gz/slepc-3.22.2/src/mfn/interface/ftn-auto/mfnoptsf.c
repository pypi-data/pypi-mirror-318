#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* mfnopts.c */
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
#define mfnsetfromoptions_ MFNSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetfromoptions_ mfnsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngettolerances_ MFNGETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngettolerances_ mfngettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsettolerances_ MFNSETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsettolerances_ mfnsettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetdimensions_ MFNGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetdimensions_ mfngetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsetdimensions_ MFNSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetdimensions_ mfnsetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnseterrorifnotconverged_ MFNSETERRORIFNOTCONVERGED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnseterrorifnotconverged_ mfnseterrorifnotconverged
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngeterrorifnotconverged_ MFNGETERRORIFNOTCONVERGED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngeterrorifnotconverged_ mfngeterrorifnotconverged
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsetoptionsprefix_ MFNSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetoptionsprefix_ mfnsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnappendoptionsprefix_ MFNAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnappendoptionsprefix_ mfnappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetoptionsprefix_ MFNGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetoptionsprefix_ mfngetoptionsprefix
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  mfnsetfromoptions_(MFN mfn, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNSetFromOptions(
	(MFN)PetscToPointer((mfn) ));
}
SLEPC_EXTERN void  mfngettolerances_(MFN mfn,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(maxits);
*ierr = MFNGetTolerances(
	(MFN)PetscToPointer((mfn) ),tol,maxits);
}
SLEPC_EXTERN void  mfnsettolerances_(MFN mfn,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNSetTolerances(
	(MFN)PetscToPointer((mfn) ),*tol,*maxits);
}
SLEPC_EXTERN void  mfngetdimensions_(MFN mfn,PetscInt *ncv, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLINTEGER(ncv);
*ierr = MFNGetDimensions(
	(MFN)PetscToPointer((mfn) ),ncv);
}
SLEPC_EXTERN void  mfnsetdimensions_(MFN mfn,PetscInt *ncv, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNSetDimensions(
	(MFN)PetscToPointer((mfn) ),*ncv);
}
SLEPC_EXTERN void  mfnseterrorifnotconverged_(MFN mfn,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNSetErrorIfNotConverged(
	(MFN)PetscToPointer((mfn) ),*flg);
}
SLEPC_EXTERN void  mfngeterrorifnotconverged_(MFN mfn,PetscBool *flag, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNGetErrorIfNotConverged(
	(MFN)PetscToPointer((mfn) ),flag);
}
SLEPC_EXTERN void  mfnsetoptionsprefix_(MFN mfn, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(mfn);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = MFNSetOptionsPrefix(
	(MFN)PetscToPointer((mfn) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  mfnappendoptionsprefix_(MFN mfn, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(mfn);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = MFNAppendOptionsPrefix(
	(MFN)PetscToPointer((mfn) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  mfngetoptionsprefix_(MFN mfn, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNGetOptionsPrefix(
	(MFN)PetscToPointer((mfn) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
#if defined(__cplusplus)
}
#endif
