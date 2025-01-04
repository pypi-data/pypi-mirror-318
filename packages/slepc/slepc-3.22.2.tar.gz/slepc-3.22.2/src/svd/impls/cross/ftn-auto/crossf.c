#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* cross.c */
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

#include "slepcsvd.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdcrosssetexplicitmatrix_ SVDCROSSSETEXPLICITMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdcrosssetexplicitmatrix_ svdcrosssetexplicitmatrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdcrossgetexplicitmatrix_ SVDCROSSGETEXPLICITMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdcrossgetexplicitmatrix_ svdcrossgetexplicitmatrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdcrossseteps_ SVDCROSSSETEPS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdcrossseteps_ svdcrossseteps
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdcrossgeteps_ SVDCROSSGETEPS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdcrossgeteps_ svdcrossgeteps
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  svdcrosssetexplicitmatrix_(SVD svd,PetscBool *explicitmat, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDCrossSetExplicitMatrix(
	(SVD)PetscToPointer((svd) ),*explicitmat);
}
SLEPC_EXTERN void  svdcrossgetexplicitmatrix_(SVD svd,PetscBool *explicitmat, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDCrossGetExplicitMatrix(
	(SVD)PetscToPointer((svd) ),explicitmat);
}
SLEPC_EXTERN void  svdcrossseteps_(SVD svd,EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(eps);
*ierr = SVDCrossSetEPS(
	(SVD)PetscToPointer((svd) ),
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  svdcrossgeteps_(SVD svd,EPS *eps, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
PetscBool eps_null = !*(void**) eps ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(eps);
*ierr = SVDCrossGetEPS(
	(SVD)PetscToPointer((svd) ),eps);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! eps_null && !*(void**) eps) * (void **) eps = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
